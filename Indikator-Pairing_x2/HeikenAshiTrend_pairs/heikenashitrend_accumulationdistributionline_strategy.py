import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HeikenAshiTrend_AccumulationDistributionLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HeikenAshiTrend und AccumulationDistributionLine
    """
    
    params = (
        ('indicators', {
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            },
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            }
        }),
        ('weights', {
            'HeikenAshiTrend': 1.0,
            'AccumulationDistributionLine': 1.0
        })
    )
