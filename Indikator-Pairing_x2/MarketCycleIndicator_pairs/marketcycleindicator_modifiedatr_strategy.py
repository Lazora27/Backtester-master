import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketCycleIndicator_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketCycleIndicator und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'MarketCycleIndicator': {
                'class': MarketCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketCycleIndicator'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'MarketCycleIndicator': 1.0,
            'ModifiedATR': 1.0
        })
    )
