import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeMomentumIndex_GannFans_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeMomentumIndex und GannFans
    """
    
    params = (
        ('indicators', {
            'RelativeMomentumIndex': {
                'class': RelativeMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeMomentumIndex'>
            },
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            }
        }),
        ('weights', {
            'RelativeMomentumIndex': 1.0,
            'GannFans': 1.0
        })
    )
