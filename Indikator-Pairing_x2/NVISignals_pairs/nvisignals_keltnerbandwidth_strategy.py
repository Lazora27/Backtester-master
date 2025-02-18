import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
