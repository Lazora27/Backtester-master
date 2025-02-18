import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_MarketCycleIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und MarketCycleIndicator
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'MarketCycleIndicator': {
                'class': MarketCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketCycleIndicator'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'MarketCycleIndicator': 1.0
        })
    )
