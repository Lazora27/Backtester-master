import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_AccumulationDistributionLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und AccumulationDistributionLine
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'AccumulationDistributionLine': 1.0
        })
    )
