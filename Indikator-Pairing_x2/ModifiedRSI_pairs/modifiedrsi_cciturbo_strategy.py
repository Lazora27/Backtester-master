import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und CCITurbo
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'CCITurbo': 1.0
        })
    )
