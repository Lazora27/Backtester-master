import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
