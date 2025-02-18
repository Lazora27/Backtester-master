import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeKrollStop_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeKrollStop und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'ChandeKrollStop': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
