import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeMomentumIndex_GannAngles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeMomentumIndex und GannAngles
    """
    
    params = (
        ('indicators', {
            'RelativeMomentumIndex': {
                'class': RelativeMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeMomentumIndex'>
            },
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            }
        }),
        ('weights', {
            'RelativeMomentumIndex': 1.0,
            'GannAngles': 1.0
        })
    )
