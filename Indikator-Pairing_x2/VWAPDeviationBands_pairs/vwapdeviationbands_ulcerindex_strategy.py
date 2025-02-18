import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPDeviationBands_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPDeviationBands und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'VWAPDeviationBands': 1.0,
            'UlcerIndex': 1.0
        })
    )
