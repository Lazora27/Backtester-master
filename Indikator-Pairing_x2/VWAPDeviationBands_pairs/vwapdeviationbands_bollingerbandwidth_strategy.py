import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPDeviationBands_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPDeviationBands und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'VWAPDeviationBands': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
