import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketCycleIndicator_ProjectionOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketCycleIndicator und ProjectionOscillator
    """
    
    params = (
        ('indicators', {
            'MarketCycleIndicator': {
                'class': MarketCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketCycleIndicator'>
            },
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            }
        }),
        ('weights', {
            'MarketCycleIndicator': 1.0,
            'ProjectionOscillator': 1.0
        })
    )
