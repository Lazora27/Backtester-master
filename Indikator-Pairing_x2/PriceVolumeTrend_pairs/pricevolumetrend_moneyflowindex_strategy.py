import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceVolumeTrend_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceVolumeTrend und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'PriceVolumeTrend': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
