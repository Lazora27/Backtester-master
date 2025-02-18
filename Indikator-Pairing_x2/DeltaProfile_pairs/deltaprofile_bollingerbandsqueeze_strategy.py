import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_BollingerBandSqueeze_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und BollingerBandSqueeze
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'BollingerBandSqueeze': 1.0
        })
    )
