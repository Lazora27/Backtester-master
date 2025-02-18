import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeVigorIndex_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeVigorIndex und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'RelativeVigorIndex': 1.0,
            'EhlersDecycler': 1.0
        })
    )
