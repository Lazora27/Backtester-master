import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeVigorIndex_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeVigorIndex und CCITurbo
    """
    
    params = (
        ('indicators', {
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'RelativeVigorIndex': 1.0,
            'CCITurbo': 1.0
        })
    )
