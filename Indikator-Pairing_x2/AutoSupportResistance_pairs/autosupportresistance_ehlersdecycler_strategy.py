import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'EhlersDecycler': 1.0
        })
    )
