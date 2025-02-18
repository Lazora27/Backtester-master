import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_GannSquareReversal_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und GannSquareReversal
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'GannSquareReversal': 1.0
        })
    )
