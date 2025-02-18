import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPDeviationBands_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPDeviationBands und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'VWAPDeviationBands': 1.0,
            'EhlersDecycler': 1.0
        })
    )
