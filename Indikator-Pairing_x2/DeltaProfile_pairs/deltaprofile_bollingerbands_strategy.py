import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und BollingerBands
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'BollingerBands': 1.0
        })
    )
