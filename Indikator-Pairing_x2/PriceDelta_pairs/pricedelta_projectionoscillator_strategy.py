import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_ProjectionOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und ProjectionOscillator
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'ProjectionOscillator': 1.0
        })
    )
