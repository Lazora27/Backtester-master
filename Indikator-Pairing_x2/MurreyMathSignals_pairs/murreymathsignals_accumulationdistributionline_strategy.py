import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathSignals_AccumulationDistributionLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathSignals und AccumulationDistributionLine
    """
    
    params = (
        ('indicators', {
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            },
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            }
        }),
        ('weights', {
            'MurreyMathSignals': 1.0,
            'AccumulationDistributionLine': 1.0
        })
    )
