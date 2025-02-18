import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'EhlersDecycler': 1.0
        })
    )
