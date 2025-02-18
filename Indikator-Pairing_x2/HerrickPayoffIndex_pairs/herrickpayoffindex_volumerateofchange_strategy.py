import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HerrickPayoffIndex_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HerrickPayoffIndex und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'HerrickPayoffIndex': {
                'class': HerrickPayoffIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HerrickPayoffIndex'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'HerrickPayoffIndex': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
