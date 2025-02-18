import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolatilityIndex_VWAPDeviationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolatilityIndex und VWAPDeviationBands
    """
    
    params = (
        ('indicators', {
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            },
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            }
        }),
        ('weights', {
            'VolatilityIndex': 1.0,
            'VWAPDeviationBands': 1.0
        })
    )
