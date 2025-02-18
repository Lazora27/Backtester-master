import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'EhlersDecycler': 1.0
        })
    )
