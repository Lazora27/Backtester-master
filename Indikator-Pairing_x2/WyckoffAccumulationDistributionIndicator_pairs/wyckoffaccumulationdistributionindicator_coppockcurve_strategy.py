import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WyckoffAccumulationDistributionIndicator_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WyckoffAccumulationDistributionIndicator und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'WyckoffAccumulationDistributionIndicator': {
                'class': WyckoffAccumulationDistributionIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WyckoffAccumulationDistributionIndicator'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'WyckoffAccumulationDistributionIndicator': 1.0,
            'CoppockCurve': 1.0
        })
    )
