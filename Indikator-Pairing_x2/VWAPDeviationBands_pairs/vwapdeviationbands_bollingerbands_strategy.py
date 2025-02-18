import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPDeviationBands_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPDeviationBands und BollingerBands
    """
    
    params = (
        ('indicators', {
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'VWAPDeviationBands': 1.0,
            'BollingerBands': 1.0
        })
    )
