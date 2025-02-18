import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketCycleIndicator_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketCycleIndicator und CCITurbo
    """
    
    params = (
        ('indicators', {
            'MarketCycleIndicator': {
                'class': MarketCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketCycleIndicator'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'MarketCycleIndicator': 1.0,
            'CCITurbo': 1.0
        })
    )
