import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_VWAPDeviationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und VWAPDeviationBands
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'VWAPDeviationBands': 1.0
        })
    )
