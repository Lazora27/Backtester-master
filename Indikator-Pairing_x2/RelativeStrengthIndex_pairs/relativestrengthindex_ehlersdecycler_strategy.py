import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeStrengthIndex_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeStrengthIndex und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'RelativeStrengthIndex': {
                'class': RelativeStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeStrengthIndex1'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'RelativeStrengthIndex': 1.0,
            'EhlersDecycler': 1.0
        })
    )
