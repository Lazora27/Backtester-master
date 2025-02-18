import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeMomentumIndex_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeMomentumIndex und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'RelativeMomentumIndex': {
                'class': RelativeMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeMomentumIndex'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'RelativeMomentumIndex': 1.0,
            'EhlersDecycler': 1.0
        })
    )
