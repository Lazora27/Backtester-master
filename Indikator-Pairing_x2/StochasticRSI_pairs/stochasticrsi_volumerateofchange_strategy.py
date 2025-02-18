import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
