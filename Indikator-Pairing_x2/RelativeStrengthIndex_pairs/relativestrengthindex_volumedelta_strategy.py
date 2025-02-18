import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeStrengthIndex_VolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeStrengthIndex und VolumeDelta
    """
    
    params = (
        ('indicators', {
            'RelativeStrengthIndex': {
                'class': RelativeStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeStrengthIndex1'>
            },
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            }
        }),
        ('weights', {
            'RelativeStrengthIndex': 1.0,
            'VolumeDelta': 1.0
        })
    )
