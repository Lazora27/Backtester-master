import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_MurreyMathLines_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und MurreyMathLines
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'MurreyMathLines': 1.0
        })
    )
