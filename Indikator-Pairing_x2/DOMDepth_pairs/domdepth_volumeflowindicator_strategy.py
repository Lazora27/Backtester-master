import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_VolumeFlowIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und VolumeFlowIndicator
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'VolumeFlowIndicator': {
                'class': VolumeFlowIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeFlowIndicator'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'VolumeFlowIndicator': 1.0
        })
    )
