import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerBandWidth_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerBandWidth und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'KeltnerBandWidth': 1.0,
            'EhlersDecycler': 1.0
        })
    )
