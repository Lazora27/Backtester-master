import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_ModifiedRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und ModifiedRSI
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'ModifiedRSI': 1.0
        })
    )
