import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_EhlersInstantaneousTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und EhlersInstantaneousTrendline
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'EhlersInstantaneousTrendline': {
                'class': EhlersInstantaneousTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersInstantaneousTrendline'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'EhlersInstantaneousTrendline': 1.0
        })
    )
