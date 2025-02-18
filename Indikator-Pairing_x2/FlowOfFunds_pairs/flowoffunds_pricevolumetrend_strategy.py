import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FlowOfFunds_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FlowOfFunds und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'FlowOfFunds': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
