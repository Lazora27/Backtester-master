import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
