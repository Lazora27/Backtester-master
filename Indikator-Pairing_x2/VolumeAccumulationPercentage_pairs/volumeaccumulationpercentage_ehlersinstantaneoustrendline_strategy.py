import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeAccumulationPercentage_EhlersInstantaneousTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeAccumulationPercentage und EhlersInstantaneousTrendline
    """
    
    params = (
        ('indicators', {
            'VolumeAccumulationPercentage': {
                'class': VolumeAccumulationPercentage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeAccumulationPercentage'>
            },
            'EhlersInstantaneousTrendline': {
                'class': EhlersInstantaneousTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersInstantaneousTrendline'>
            }
        }),
        ('weights', {
            'VolumeAccumulationPercentage': 1.0,
            'EhlersInstantaneousTrendline': 1.0
        })
    )
