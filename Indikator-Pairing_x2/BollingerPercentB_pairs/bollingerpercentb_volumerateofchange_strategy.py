import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerPercentB_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerPercentB und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'BollingerPercentB': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
