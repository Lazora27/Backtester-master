import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'ParabolicSAR': 1.0
        })
    )
