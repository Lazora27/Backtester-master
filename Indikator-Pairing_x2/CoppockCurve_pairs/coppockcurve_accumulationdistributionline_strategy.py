import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_AccumulationDistributionLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und AccumulationDistributionLine
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'AccumulationDistributionLine': 1.0
        })
    )
