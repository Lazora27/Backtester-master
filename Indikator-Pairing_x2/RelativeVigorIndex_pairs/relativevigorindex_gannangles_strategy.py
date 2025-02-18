import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeVigorIndex_GannAngles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeVigorIndex und GannAngles
    """
    
    params = (
        ('indicators', {
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            },
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            }
        }),
        ('weights', {
            'RelativeVigorIndex': 1.0,
            'GannAngles': 1.0
        })
    )
