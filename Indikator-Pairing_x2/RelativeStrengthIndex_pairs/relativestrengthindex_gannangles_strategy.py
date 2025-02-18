import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeStrengthIndex_GannAngles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeStrengthIndex und GannAngles
    """
    
    params = (
        ('indicators', {
            'RelativeStrengthIndex': {
                'class': RelativeStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeStrengthIndex1'>
            },
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            }
        }),
        ('weights', {
            'RelativeStrengthIndex': 1.0,
            'GannAngles': 1.0
        })
    )
