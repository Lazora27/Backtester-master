import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceVolumeTrend_AccumulationDistributionLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceVolumeTrend und AccumulationDistributionLine
    """
    
    params = (
        ('indicators', {
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            },
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            }
        }),
        ('weights', {
            'PriceVolumeTrend': 1.0,
            'AccumulationDistributionLine': 1.0
        })
    )
