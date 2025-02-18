import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
