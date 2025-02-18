import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_VolumeFlowIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und VolumeFlowIndicator
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'VolumeFlowIndicator': {
                'class': VolumeFlowIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeFlowIndicator'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'VolumeFlowIndicator': 1.0
        })
    )
