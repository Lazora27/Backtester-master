import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeVigorIndex_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeVigorIndex und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'RelativeVigorIndex': 1.0,
            'CenterOfGravity': 1.0
        })
    )
