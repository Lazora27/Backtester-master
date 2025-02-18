import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsAccumulationDistribution_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsAccumulationDistribution und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'WilliamsAccumulationDistribution': {
                'class': WilliamsAccumulationDistribution,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsAccumulationDistribution'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'WilliamsAccumulationDistribution': 1.0,
            'CoppockCurve': 1.0
        })
    )
