import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_GannSquares_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und GannSquares
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'GannSquares': 1.0
        })
    )
