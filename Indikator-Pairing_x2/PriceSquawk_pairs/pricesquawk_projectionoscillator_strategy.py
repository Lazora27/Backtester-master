import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_ProjectionOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und ProjectionOscillator
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'ProjectionOscillator': 1.0
        })
    )
